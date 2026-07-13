from pathlib import Path
import pandas as pd


class Cleaner:
    """
    Clase encargada de limpiar y transformar los datasets del proyecto.

    Cada dataset posee su propio pipeline de limpieza, apoyándose en
    funciones auxiliares reutilizables.
    """

    # ==========================================================
    # Columnas porcentuales del dataset principal
    # ==========================================================

    PERCENT_COLUMNS_PRINCIPAL = [
        "TASA_MATRICULACIÓN_5_16",
        "COBERTURA_NETA",
        "COBERTURA_NETA_TRANSICIÓN",
        "COBERTURA_NETA_PRIMARIA",
        "COBERTURA_NETA_SECUNDARIA",
        "COBERTURA_NETA_MEDIA",
        "COBERTURA_BRUTA",
        "COBERTURA_BRUTA_TRANSICIÓN",
        "COBERTURA_BRUTA_PRIMARIA",
        "COBERTURA_BRUTA_SECUNDARIA",
        "COBERTURA_BRUTA_MEDIA",
        "DESERCIÓN",
        "DESERCIÓN_TRANSICIÓN",
        "DESERCIÓN_PRIMARIA",
        "DESERCIÓN_SECUNDARIA",
        "DESERCIÓN_MEDIA",
        "APROBACIÓN",
        "APROBACIÓN_TRANSICIÓN",
        "APROBACIÓN_PRIMARIA",
        "APROBACIÓN_SECUNDARIA",
        "APROBACIÓN_MEDIA",
        "REPROBACIÓN",
        "REPROBACIÓN_TRANSICIÓN",
        "REPROBACIÓN_PRIMARIA",
        "REPROBACIÓN_SECUNDARIA",
        "REPROBACIÓN_MEDIA",
        "REPITENCIA",
        "REPITENCIA_TRANSICIÓN",
        "REPITENCIA_PRIMARIA",
        "REPITENCIA_SECUNDARIA",
        "REPITENCIA_MEDIA",
        "SEDES_CONECTADAS_A_INTERNET"
    ]

    def __init__(self):

        project_root = Path.cwd()

        self.output_dir = project_root / "data" / "processed"
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # ==========================================================
    # FUNCIONES AUXILIARES
    # ==========================================================

    @staticmethod
    def _remove_percent(series):
        """
        Elimina el símbolo %.
        """
        return (
            series.astype(str)
                .str.replace("%", "", regex=False)
                .str.strip()
                .replace({"nan": pd.NA})
        )


    @staticmethod
    def _remove_thousand_separator(series):
        """
        Elimina separadores de miles.
        """
        return (
            series.astype(str)
                .str.replace(",", "", regex=False)
                .replace({"nan": pd.NA})
        )


    @staticmethod
    def _replace_decimal_comma(series):
        """
        Convierte coma decimal a punto decimal.
        """
        return (
            series.astype(str)
                .str.replace(",", ".", regex=False)
                .replace({"nan": pd.NA})
        )


    @staticmethod
    def _convert_numeric(series):
        """
        Convierte una serie a numérica.
        """
        return pd.to_numeric(series, errors="coerce")


    @staticmethod
    def _create_year_column(df):

        df["FECHA"] = pd.to_datetime(
            df["FECHA"],
            dayfirst=True,
            errors="coerce"
        )

        df["AÑO"] = df["FECHA"].dt.year

        return df


    @staticmethod
    def _drop_duplicate_keys(df, keys):

        return df.drop_duplicates(
            subset=keys,
            keep="first"
        )


    def _clean_numeric_column(
        self,
        series,
        remove_percent=False,
        remove_thousand=False,
        replace_decimal_comma=False,
    ):
        """
        Pipeline genérico para limpiar columnas numéricas.
        """

        if remove_percent:
            series = self._remove_percent(series)

        if remove_thousand:
            series = self._remove_thousand_separator(series)

        if replace_decimal_comma:
            series = self._replace_decimal_comma(series)

        return self._convert_numeric(series)
    

    #Principal dataset cleaning function
    def clean_principal(self, df):

        df = df.copy()

        print("Limpiando dataset principal...")

        # ======================
        # Porcentajes
        # ======================

        for col in self.PERCENT_COLUMNS_PRINCIPAL:

            if col in df.columns:

                df[col] = self._clean_numeric_column(
                    df[col],
                    remove_percent=True
                )

        # ======================
        # Población
        # ======================

        df["POBLACIÓN_5_16"] = self._clean_numeric_column(
            df["POBLACIÓN_5_16"],
            remove_thousand=True
        )

        # ======================
        # Tamaño promedio
        # ======================

        df["TAMAÑO_PROMEDIO_DE_GRUPO"] = self._clean_numeric_column(
            df["TAMAÑO_PROMEDIO_DE_GRUPO"],
            remove_percent=True,
            replace_decimal_comma=True
        )

        print("Dataset principal limpio.")

        return df
    
    #Cleaning function for PAE dataset
    def clean_pae(self, df):

        df = df.copy()

        print("Limpiando dataset PAE...")

        df = self._create_year_column(df)

        df["CANTIDAD_BENEFICIARIOS_PAE"] = (
            self._clean_numeric_column(
                df["CANTIDAD_BENEFICIARIOS_PAE"],
                remove_thousand=True
            )
        )

        print("Dataset PAE limpio.")

        return df
    
    #Cleaning function for ETC dataset
    def clean_etc(self, df):

        df = df.copy()

        print("Limpiando dataset ETC...")

        # ======================
        # Duplicado conocido
        # ======================

        df = self._drop_duplicate_keys(
            df,
            ["AÑO", "CÓDIGO_ETC"]
        )

        # ======================
        # Población
        # ======================

        df["POBLACIÓN_5_16"] = self._clean_numeric_column(
            df["POBLACIÓN_5_16"],
            remove_thousand=True
        )

        # ======================
        # Tasa
        # ======================

        df["TASA_MATRICULACIÓN_5_16"] = (
            self._clean_numeric_column(
                df["TASA_MATRICULACIÓN_5_16"],
                remove_percent=True
            )
        )

        # ======================
        # Internet
        # ======================

        df["SEDES_CONECTADAS_A_INTERNET"] = (
            self._clean_numeric_column(
                df["SEDES_CONECTADAS_A_INTERNET"],
                remove_percent=True
            )
        )

        # ======================
        # Tamaño promedio
        # ======================

        df["TAMAÑO_PROMEDIO_DE_GRUPO"] = (
            self._clean_numeric_column(
                df["TAMAÑO_PROMEDIO_DE_GRUPO"],
                replace_decimal_comma=True
            )
        )

        print("Dataset ETC limpio.")

        return df
    
   # GUARDAR 
    def save_dataset(self, df, filename): 
        path = self.output_dir / filename 
        df.to_csv(path, index=False) 
        print(f"Dataset guardado en:\n{path}")
from typing import List

import pandas as pd


class DataValidator:
    """
    Clase para validar la calidad de los datasets.

    Este módulo NO modifica los datos.
    Únicamente inspecciona y reporta posibles problemas.
    """

    @staticmethod
    def dataset_shape(df: pd.DataFrame):
        """
        Retorna el número de filas y columnas.
        """
        return df.shape

    @staticmethod
    def column_types(df: pd.DataFrame):
        """
        Retorna los tipos de datos de todas las columnas.
        """
        return df.dtypes

    @staticmethod
    def missing_values(df: pd.DataFrame):
        """
        Retorna únicamente las columnas con valores faltantes.
        """
        missing = df.isnull().sum()
        return missing[missing > 0].sort_values(ascending=False)

    @staticmethod
    def duplicated_rows(df: pd.DataFrame):
        """
        Número de filas completamente duplicadas.
        """
        return df.duplicated().sum()

    @staticmethod
    def duplicated_keys(df: pd.DataFrame, keys: List[str]):
        """
        Número de registros duplicados según una llave.
        """
        return df.duplicated(subset=keys).sum()

    @staticmethod
    def unique_values(df: pd.DataFrame):
        """
        Número de valores únicos por columna.
        """
        return df.nunique()

    @staticmethod
    def column_summary(df: pd.DataFrame):
        """
        Genera un resumen por columna.
        """

        return pd.DataFrame({
            "dtype": df.dtypes,
            "missing": df.isnull().sum(),
            "missing_%": (df.isnull().mean() * 100).round(2),
            "unique_values": df.nunique()
        })

    @staticmethod
    def sample_values(
        df: pd.DataFrame,
        column: str,
        n: int = 10
    ):
        """
        Muestra algunos valores distintos de una columna.
        Muy útil para inspeccionar formatos.
        """
        return df[column].dropna().unique()[:n]

    @staticmethod
    def validate_keys(
        df: pd.DataFrame,
        keys: List[str]
    ):
        """
        Valida una llave candidata para utilizarla en merges.
        """

        missing_columns = [
            col for col in keys if col not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"No existen las columnas: {missing_columns}"
            )

        duplicated = df.duplicated(subset=keys).sum()

        nulls = (
            df[keys]
            .isnull()
            .sum()
            .rename("null_values")
        )

        summary = {
            "keys": keys,
            "rows": len(df),
            "unique_combinations": len(df[keys].drop_duplicates()),
            "duplicated_keys": duplicated,
            "has_nulls": bool(nulls.sum() > 0),
            "null_values": nulls
        }

        return summary
    
    @staticmethod
    def numeric_candidates(df: pd.DataFrame):
        """
        Detecta columnas de tipo object que probablemente contienen
        información numérica almacenada como texto.

        Analiza si contienen porcentajes, números enteros o decimales
        escritos como cadenas.

        Returns
        -------
        pd.DataFrame
            Resumen de las columnas candidatas a conversión numérica.
        """

        results = []

        for column in df.columns:

            if df[column].dtype != "object":
                continue

            # Eliminar nulos y convertir a string
            values = df[column].dropna().astype(str)

            if values.empty:
                continue

            # Revisar si contiene porcentaje
            has_percent = values.str.contains("%").any()

            # Eliminar caracteres comunes para intentar convertir
            cleaned = (
                values
                .str.replace("%", "", regex=False)
                .str.replace(",", "", regex=False)
                .str.strip()
            )

            numeric = pd.to_numeric(cleaned, errors="coerce")

            conversion_rate = (
                numeric.notna().sum() / len(values)
            ) * 100

            if conversion_rate >= 90:

                results.append({
                    "column": column,
                    "current_dtype": str(df[column].dtype),
                    "conversion_rate_%": round(conversion_rate, 2),
                    "contains_percent": has_percent,
                    "sample": values.iloc[0]
                })

        return pd.DataFrame(results)
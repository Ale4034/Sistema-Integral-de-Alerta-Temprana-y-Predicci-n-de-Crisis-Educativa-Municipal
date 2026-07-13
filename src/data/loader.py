from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Clase para cargar e inspeccionar los datasets del proyecto.
    """

    def __init__(self, data_dir):
        """
        Parameters
        ----------
        data_dir : str o Path
            Ruta a la carpeta donde se encuentran los datasets.
        """
        self.data_dir = Path(data_dir)

        if not self.data_dir.exists():
            raise FileNotFoundError(
                f"La carpeta de datos no existe:\n{self.data_dir}"
            )

        print(f"📂 Carpeta de datos: {self.data_dir}")

    def _load_csv(self, filename, **kwargs):
        """
        Carga un archivo CSV.
        """

        path = self.data_dir / filename

        if not path.exists():
            raise FileNotFoundError(
                f"No se encontró el archivo:\n{path}"
            )

        print(f"\n📄 Cargando {filename}...")

        df = pd.read_csv(
            path,
            dtype={
                "CÓDIGO_ETC": "string",
                "CÓDIGO_MUNICIPIO": "string",
                "CÓDIGO_DEPARTAMENTO": "string",
                "CODIGO_MUNICIPIO": "string",
                "CODIGO_DEPARTAMENTO": "string",
            },
            **kwargs
        )

        print("✅ Carga completada")
        print(f"   Filas: {df.shape[0]:,}")
        print(f"   Columnas: {df.shape[1]}")

        return df

    def load_principal(self):
        return self._load_csv("principal.csv")

    def load_pae(self):
        return self._load_csv("pae.csv")

    def load_etc(self):
        return self._load_csv("etc.csv")

    def load_all(self):

        return {
            "principal": self.load_principal(),
            "pae": self.load_pae(),
            "etc": self.load_etc()
        }
    
    def load_processed(self, filename):
        """
        Carga un dataset previamente procesado.

        Parameters
        ----------
        filename : str
            Nombre del archivo dentro de la carpeta indicada por data_dir.

        Returns
        -------
        pd.DataFrame
        """
        return self._load_csv(filename)
    
    def load_all_processed(self):
        """
        Carga todos los datasets procesados.
        """

        return {
            "principal": self.load_processed("principal_clean.csv"),
            "pae": self.load_processed("pae_clean.csv"),
            "etc": self.load_processed("etc_clean.csv"),
        }
    

    @staticmethod
    def summary(df, name="Dataset"):

        print("\n" + "=" * 60)
        print(f"📊 {name}")
        print("=" * 60)

        print(f"Filas: {df.shape[0]:,}")
        print(f"Columnas: {df.shape[1]}")

        memory = df.memory_usage(deep=True).sum() / (1024**2)
        print(f"Memoria: {memory:.2f} MB")

        print("\nTipos de datos:")
        print(df.dtypes.value_counts())

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        print("\nValores faltantes:")

        if len(missing) == 0:
            print("No hay valores faltantes.")
        else:
            print(missing.sort_values(ascending=False))

        print(f"\nDuplicados: {df.duplicated().sum()}")

        print("=" * 60)
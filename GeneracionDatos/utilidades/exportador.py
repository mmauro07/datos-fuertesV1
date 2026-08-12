from dataclasses import asdict
import pandas as pd


class ExportadorCSV:

    def exportar(self, objetos, nombre_archivo, tipos=None):

        registros = []

        for objeto in objetos:
            registros.append(self._aplanar(objeto))

        df = pd.DataFrame(registros)

        if tipos is not None:
            self._convertir_tipos(df, tipos)

        df.to_csv(
            f"salida/{nombre_archivo}.csv",
            index=False,
            encoding="utf-8-sig"
        )

    def _aplanar(self, objeto):

        datos = asdict(objeto)

        registro = {}

        for clave, valor in datos.items():

            if isinstance(valor, dict):
                registro.update(valor)
            else:
                registro[clave] = valor

        return registro

    def _convertir_tipos(self, df, tipos):

        for columna, tipo in tipos.items():

            if columna in df.columns:
                df[columna] = df[columna].astype(tipo)
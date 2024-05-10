### Spendr API
_Una API para crear un administrador de gastos_

[![](https://img.shields.io/badge/Live_preview-8A2BE2?color=darkgreen)]()

Para ejecutar este proyecto es necesario:

* Crear un archivo .env para agregar la variable de entorno "MONGO_URI" que es el string de conexion para la base de datos de Mongo
```bash
echo "FIREBASE_DB_URL=https://firebaseproject..." > .env
```

* Crear un entorno virtual de Python:
```bash
python3 -m venv venv
```

* Ingresar al entorno virtual:
```bash
#Linux
source ./venv/bin/activate

#Windows
.\venv\Scripts\activate
```

* Instalar los paquetes:
```bash
pip install -r requirements.txt
```

* Ejecutar el proyecto:
```bash
uvicorn main:app --host 0.0.0.0 --port 5000
```

Peticiones que se pueden hacer de acuerdo a las rutas:

* **GET /certs**: Obtienes todos los registros almacenadas en base de datos.
* **GET /cert/{id}**: Obtienes un registro definido desde la base de datos.

---
* **POST /certs**: Para ingresar datos a la base de datos de acuerdo al modelo:

```JSON
// JSON De ejemplo para realizar un POST
  {
      "name"      : "Conviértete en administrador de seguridad junior",
      "platform"  : "LinkedIn",
      "date"      : "02/05/2024",
      "id"        : "2e4260573f69fb8f420751c3d648bc0c466b483b53e5a707003ab7ef961385c1",
      "category"  : "Itinerario / Ruta de aprendizaje",
      "imageUrl"  : "https://media.licdn.com/dms/image/D4E22AQGouBDkNXZ24w/feedshare-shrink_1280/0/1714665281039?e=1718236800&v=beta&t=zUWhSYvudvKJGs8aj5-xATnscYXTxfX7XWCxvuoscIs"
  }
```

* **PUT /cert/{id}**: Para actualizar un registro en la base de datos

---
* **DELETE /cert/{id}**: Para eliminar un registro de la base de datos
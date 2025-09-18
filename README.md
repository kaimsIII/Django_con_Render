# Sistema de Registro de Usuarios con Django

Un sistema completo de registro y autenticación de usuarios desarrollado con Django, PostgreSQL y Bootstrap 5.

## 🚀 Características

- ✅ Registro de usuarios con validación
- ✅ Sistema de autenticación (login/logout)
- ✅ Interfaz atractiva con Bootstrap 5
- ✅ Base de datos PostgreSQL
- ✅ Dashboard personalizado
- ✅ Perfil de usuario detallado
- ✅ Diseño responsive
- ✅ Mensajes informativos
- ✅ Panel de administración personalizado

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 5.2.6
- **Base de Datos**: PostgreSQL
- **Frontend**: Bootstrap 5.3.2, HTML5, CSS3, JavaScript
- **Iconos**: Bootstrap Icons
- **Python**: 3.8+

## 📋 Requisitos Previos

- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)

## 🔧 Instalación

### 1. Clonar el repositorio (o usar los archivos existentes)
```bash
# Si ya tienes los archivos, omite este paso
```

### 2. Crear un entorno virtual
```bash
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

1. Instala PostgreSQL en tu sistema
2. Crea una base de datos:
```sql
CREATE DATABASE user_registration_db;
CREATE USER postgres WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE user_registration_db TO postgres;
```

3. Actualiza las credenciales en `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_registration_db',
        'USER': 'postgres',
        'PASSWORD': 'tu_password',  # Cambia por tu contraseña
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

### 8. Acceder a la aplicación
- **Aplicación principal**: http://127.0.0.1:8000/
- **Panel de administración**: http://127.0.0.1:8000/admin/

## 📖 Uso

### Funcionalidades disponibles:

1. **Página Principal**: Vista de bienvenida con información del sistema
2. **Registro**: Crear nueva cuenta con validación completa
3. **Login**: Iniciar sesión con usuario y contraseña
4. **Dashboard**: Panel principal para usuarios autenticados
5. **Perfil**: Vista detallada del perfil del usuario
6. **Admin**: Panel de administración de Django personalizado

### Rutas disponibles:

- `/` - Página principal
- `/register/` - Registro de usuarios
- `/login/` - Inicio de sesión
- `/logout/` - Cerrar sesión
- `/dashboard/` - Dashboard de usuario
- `/profile/` - Perfil de usuario
- `/admin/` - Panel de administración

## 🎨 Características de la Interfaz

- **Diseño Responsive**: Compatible con dispositivos móviles y desktop
- **Bootstrap 5**: Framework CSS moderno
- **Iconos**: Bootstrap Icons para mejorar la experiencia visual
- **Animaciones**: Transiciones suaves y efectos visuales
- **Validación**: Validación en tiempo real de formularios
- **Mensajes**: Sistema de notificaciones para el usuario

## 🔒 Seguridad

- Validación de contraseñas con requisitos de seguridad
- Protección CSRF en todos los formularios
- Autenticación requerida para páginas privadas
- Hash seguro de contraseñas
- Validación de datos en backend y frontend

## 📁 Estructura del Proyecto

```
user_registration/
│
├── accounts/                 # Aplicación principal
│   ├── migrations/          # Migraciones de la base de datos
│   ├── admin.py            # Configuración del admin
│   ├── forms.py            # Formularios
│   ├── models.py           # Modelos de datos
│   ├── urls.py             # URLs de la aplicación
│   └── views.py            # Vistas
│
├── static/                  # Archivos estáticos
│   └── css/
│       └── custom.css      # CSS personalizado
│
├── templates/               # Templates HTML
│   ├── base.html           # Template base
│   └── accounts/
│       ├── home.html       # Página principal
│       ├── register.html   # Registro
│       ├── login.html      # Login
│       ├── dashboard.html  # Dashboard
│       └── profile.html    # Perfil
│
├── user_registration/       # Configuración del proyecto
│   ├── settings.py         # Configuración
│   ├── urls.py            # URLs principales
│   └── wsgi.py            # WSGI
│
├── manage.py               # Script de Django
├── requirements.txt        # Dependencias
└── README.md              # Este archivo
```

## 🚀 Próximas Mejoras

- [ ] Edición de perfil de usuario
- [ ] Cambio de contraseña
- [ ] Recuperación de contraseña por email
- [ ] Verificación de email
- [ ] Subida de foto de perfil
- [ ] Sistema de roles
- [ ] API REST
- [ ] Pruebas unitarias

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 📞 Soporte

Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un issue en el repositorio.

---

**Desarrollado con ❤️ usando Django y Bootstrap**
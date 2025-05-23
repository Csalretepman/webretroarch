# WebRetroArch

**WebRetroArch** — контейнеризированная версия WebRetro с автогенерацией HTML-интерфейса для запуска NES-ромов через браузер.

## 🧩 Возможности

- 📦 Основано на [WebRetro v6.5](https://github.com/BinBashBanana/webretro/releases/tag/v6.5)
- 🔁 Автоматическое сканирование каталога `roms/` (включая подкаталоги)
- 🌐 Генерация `nes.html` со списком всех найденных `.nes`-файлов и ссылками на их запуск
- 🐳 Поддержка Docker и монтирования внешнего каталога для ROM'ов
- 🔒 Поддержка HTTPS через внешний прокси (например, Caddy или Nginx)

## 📂 Структура проекта

```bash
.
├── Dockerfile
├── generate-nes-html.py   # скрипт генерации HTML
├── nes.html               # сгенерированный интерфейс запуска
├── roms/                  # каталог с ROM-файлами (*.nes)
│   └── .gitignore         # чтобы каталог попал в git, но не содержал rom-файлы
└── ...
```
## 🚀 Запуск
```bash
docker compose up -d
```
После запуска сервис будет доступен по адресу:
http://your-host-or-ip/nes.html

### 📥 Добавление ROM'ов
Положите .nes файлы (и/или подпапки с ними) в папку roms/. Пример:

```bash
roms/
├── Contra.nes
├── Battle City.nes
└── Capcom/
    └── Mega Man 2.nes
```
⚠️ Путь к файлам должен быть корректен для запуска внутри WebRetro. Все пути учитываются при генерации HTML.

### 🔐 Настройка HTTPS (опционально)
Рекомендуется использовать внешний HTTPS-прокси, например Caddy или Nginx, с автогенерацией Let's Encrypt сертификатов. Пример для Caddy:

```caddyfile
retro.example.com {
    reverse_proxy localhost:8080
}
```
### ⚙️ Работа, проделанная в этом форке
Контейнеризация WebRetro с помощью Docker

Создание скрипта на Python для генерации nes.html с ссылками на запуск

Рекурсивный обход подкаталогов roms/ и кодирование URL для корректного отображения

Настройка Nginx внутри контейнера

Подготовка проекта к деплою за reverse proxy (например, через Caddy)

### 🧾 Лицензия
Лицензия оригинального WebRetro см. [здесь](https://github.com/BinBashBanana/webretro?tab=MIT-1-ov-file). Все модификации в этом репозитории распространяются на тех же условиях. 


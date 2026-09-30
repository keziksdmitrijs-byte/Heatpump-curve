# HVAC Weather Curve

Погодозависимая кривая температуры подачи для Home Assistant.

## Установка через HACS
1. Создайте публичный GitHub-репозиторий.
2. Загрузите в корень репозитория папку `custom_components` и файл `hacs.json`.
3. В HACS откройте **Integrations → ⋮ → Custom repositories**.
4. Добавьте URL репозитория и выберите тип **Integration**.
5. Создайте GitHub Release с тегом `v1.0.1` — одного commit или tag недостаточно.
6. Установите интеграцию и перезапустите Home Assistant.

Точки кривой: `-20:55,-10:49,0:43,10:35,15:30`. Используемый датчик наружной температуры: `sensor.outdoor_temperature`.

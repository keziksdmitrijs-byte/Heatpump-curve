# HVAC Weather Curve v1.1.0

В конфигураторе можно выбрать датчик наружной температуры и целевую сущность `number` или `input_number`. Интеграция рассчитывает температуру подачи с линейной интерполяцией и записывает её в целевую сущность.

Добавьте ресурс карточки: `/local/hvac-weather-curve-card.js`, тип `JavaScript module`. Затем используйте:

```yaml
type: custom:hvac-weather-curve-card
entity: sensor.название_calculated_flow_temperature
```

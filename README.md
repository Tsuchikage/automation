# <span style="color:#F0F8FF"> Название проекта - Automation </span>
**Система автоматического анализа упавших автотестов.**

## <span style="color:#F0F8FF"> Цели и предпосылки </span>
Проект Automation направлен на автоматический анализ упавших автотестов. Цель проекта - сократить время, затрачиваемое на ручной разбор ошибок, путем автоматического анализа причин падения автотестов.

### <span style="color:#F0F8FF"> Зачем идем в разработку продукта? </span>
**Бизнес-цель:** Создать систему, которая позволит ускорить процесс анализа упавших тестов, автоматизируя рутинные задачи и повышая общую эффективность команды.

**Преимущества использования ML:** Повышение точности анализа причин падений тестов, сокращение времени на ручной анализ и улучшение качества результатов.

**Критерии успеха:** Увеличение количества правильно определённых причин падений тестов, положительные отзывы команды, снижение времени анализа.

### <span style="color:#F0F8FF"> Бизнес-требования и ограничения </span>
**Описание Бизнес-Требований:** Подробно описаны в разделе "**Основные планируемые функции и возможности**".

**Бизнес-ограничения:** Соблюдение бюджета и сроков разработки.

**Ожидания от итерации:** Улучшение функциональности анализа автотестов.

**Описание бизнес-процесса пилота:** Интеграция модели ML в существующий процесс для улучшения анализа упавших автотестов.

**Критерии успешного пилота:** Достижение заранее определённых бизнес-метрик и положительная обратная связь от команды.


### <span style="color:#F0F8FF"> Скоуп Проекта/Итерации </span>
**Входит в Скоуп:**
- Настройка Pipeline для автоматического запуска тестов
- Настройка автоматической публикации результатов прогона тестов
- Разработка и дизайн интерфейса публикации результатов прогона автотестов
- Базовые функции поиска и фильтрации.

**Не Входит в Скоуп**
- Расширенные алгоритмы машинного обучения
- Полноценная интеграция с другими проектами внутри компании

**Описание результата:** 
- Критерии качества кода и воспроизводимости решения.

**Планируемый Технический Долг**
- Отложенная Оптимизация: Некоторые аспекты производительности и оптимизации могут быть временно отложены для ускорения запуска первой версии.
- Временные Решения: Использование временных решений для некоторых функций, которые будут улучшены в будущих итерациях.

### <span style="color:#F0F8FF"> Основные планируемые функции и возможности </span>
**Функциональность анализа тестов:**
- **Создание таблицы с результатами и причинами падения тестов:** Инструмент для представления результатов анализа в удобной форме, позволяющий быстро выявить причины падения тестов.
- **Сбор данных для обучения модели:** Сбор и хранение данных о причинах падения тестов для дальнейшего обучения и улучшения алгоритмов машинного обучения.
- **Автоматический анализ упавших автотестов:** Разработка алгоритмов для автоматического анализа причин падения тестов, что позволит сократить время на ручной разбор ошибок.

**Начальные настройки управления проектами:**
- **Интеграция с существующими CI/CD системами:** Возможность интеграции с уже используемыми системами непрерывной интеграции и доставки для автоматизации процесса запуска тестов и сбора результатов.
- **Настройка уведомлений и отчетов:** Функциональность для отправки уведомлений и отчетов о результатах анализа тестов, что позволит команде быть в курсе всех изменений и проблем.

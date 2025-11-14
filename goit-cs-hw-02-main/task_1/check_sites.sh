#!/bin/bash

# Список вебсайтів
websites=(
    "https://google.com"
    "https://facebook.com"
    "https://twitter.com"
)

# Назва лог-файлу
log_file="website_status.log"

# Очищаємо старий лог-файл
> "$log_file"

# Перевірка кожного сайту
for site in "${websites[@]}"; do
    # Отримуємо HTTP-код відповіді
    status_code=$(curl -s -o /dev/null -w "%{http_code}" -L "$site")

    # Перевіряємо код відповіді
    if [ "$status_code" -eq 200 ]; then
        echo "<$site> is UP" | tee -a "$log_file"
    else
        echo "<$site> is DOWN" | tee -a "$log_file"
    fi
done

# Повідомлення про завершення
echo "Результати перевірки збережено у файл: $log_file"

FROM python:3.12
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app
# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt ./

RUN apt-get update && apt-get install -y postgresql-client


# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt

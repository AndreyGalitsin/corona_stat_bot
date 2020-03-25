# corona_stat_bot

__main__.py: парсер, который вытаскивает с сайта https://www.worldometers.info/coronavirus/ данные о коронавирусе. Написан с помощью гайда https://towardsdatascience.com/coronavirus-track-coronavirus-in-your-country-by-displaying-notification-c914b5652088;

virtualenv: виртуальное окружение, создаётся с помощью гайда https://cloud.ibm.com/docs/openwhisk?topic=cloud-functions-prep#prep_python_local_virtenv;

statistics.zip: zip файл, в котором заархивированы __main__.py и virtualenv:

skill-Coronavirus-statistics.json: скилл чат-бота Watson Assistant.

Чтобы бот обращался к IBM Cloud Functions, нужно в скилле указать URL и добавить CF-based API key for this namespace.

Добрый день. На вопросы попытаюсь ответить без гугла.

1. Создавали ли вы многопоточные приложения?  
	a. Чем потоки отличаются от процессов?  
	b. Когда целесообразнее использовать одно и другое?  
	c. Что такое асинхронная обработка запросов?  
	d. Что такое неблокирующий веб-сервер?  

	a. не знаю  
	b. не знаю  
	с. когда ответ сервера не привязан к запросу. Тоесть клиент может получать информацию  
		от сервера в вида потока данных  
	d. сервер, который поддерживает асинхронную обработку запросов  

2. Какие вы знаете веб-сервера/веб-фреймворки на Python? С какими работали?  
	a. Чем WSGI отличается от CGI?  

	Не знаю ни одного production веб сервера на питоне. Работал с Flask, Djano, Pyramid.  
	WSGI - это протокол по которому общаются приложения на питоне с веб-серверами.  
	CGI - common gate interface, это скорее описание протокола  

3. С какими СУБД/хранилищами вы работали?  
	a. Чем различаются модели: реляционная, документная, key-value?  
	b. Приведите пример, где рационально использовать noSQL решение?  

	Работал с MySQL, Postgres, Mongo. В документных и key-value нет таблиц.  
	Я бы использовал noSQL например если бы делал rest api и нужно было  
	сохранять инфу в базу, потому что  
	проще было бы сохранять из json'а в базу.  

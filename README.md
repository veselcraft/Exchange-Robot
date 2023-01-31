# Exchange-Robot
<b>Requirements:</b>
<ul>
  <li>Python 3.7+ (Recommended 3.8.10)</li>
  <li>Aiogram 2.14+</li>
  <li>uvloop (not support at Windows)</li>
  <li>ujson</li>
  <li>cchardet</li>
  <li>aiodns</li>
  <li>aiohttp[speedups]</li>
  <li>Numberize 1.0.1</li>
  <li>Requests 2.26.0</li>
</ul>
<b>ENGLISH VERSION</b><br>
Exchange-Robot – exchange rates telegram bot. Funny fork of original ERTB to hide political things :D<br>
The bot recognizes currencies and amounts in the text, and then sends a message with other currencies. An example of a working bot: <a href="https://t.me/exchange_rates_vsk_bot">ERTB</a><br><br>
<b>An example of how the bot works:</b><br>
Your message:<br>
<pre>5 euro</pre>
Bot's answer:
<pre>🇪🇺5.0 EUR

🇨🇭5.39 CHF
🇮🇱19.73 ILS
🇺🇸6.06 USD</pre><br>
<b>Bot run</b><br>
By default, the bot is launched like this: <pre>python3 ERTB.py</pre> You can also enable logging of messages and errors to the terminal: <pre>python3 ERTB.py -l on</pre>or<br><br><pre>python3 ERTB.py --logs on</pre><br>
Below are all the arguments to run:
<table>
  <tr>
    <th>Name</th>
    <th>Argument</th>
    <th>Value</th>
    <th>Example</th>
    <th>Default</th>
  </tr>
  <tr>
    <td>Logging messages and errors to the terminal</td>
    <td><code>--logs</code> or <code>-l</code></td>
    <td><code>on</code> or <code>off</code></td>
    <td><code>python3 ERTB.py --logs on</code></td>
    <td><code>off</code></td>
  </tr>
  <tr>
    <td>Adding an administrator for the bot</td>
    <td><code>--admin</code> or <code>-a</code></td>
    <td>ID user</td>
    <td><code>python3 ERTB.py --admin 123456789</code></td>
    <td>missing</td>
  </tr>
  <tr>
    <td>Processing received messages on start</td>
    <td><code>--updates</code> or <code>-u</code></td>
    <td><code>on</code> or <code>off</code></td>
    <td><code>python3 ERTB.py --updates on</code></td>
    <td><code>off</code></td>
  </tr>
</table><br>
<b>Список команд в Телеграме для рядового пользователя</b><br><br>
<table>
  <tr>
    <th>Command</th>
    <th>Command Description</th>
  </tr>
  <tr>
    <td><code>/about</code></td>
    <td>Brief information about authors, version, source code and/or license.</td>
  </tr>
  <tr>
    <td><code>/help</code></td>
    <td>Help in using and configuring the bot.</td>
  </tr>
  <tr>
    <td><code>/settings</code></td>
    <td>Here you can set up a bot for your chat.</td>
  </tr>
  <tr>
    <td><code>/donate</code></td>
    <td>You can support the development of the bot with a dollar.</td>
  </tr>
  <tr>
    <td><code>/wrong</code></td>
    <td>Reply the message is incorrectly recognized.</td>
  </tr>
</table><br>
<b>List of commands in Telegram for developers/administrators</b><br><br>
<table>
  <tr>
    <th>Command</th>
    <th>Command Description</th>
  </tr>
  <tr>
    <td><code>/echo</code></td>
    <td>Sending messages to all chats. After the command, you need to write the text that you want to send.</td>
  </tr>
  <tr>
    <td><code>/count</code></td>
    <td>Getting information about the number of bot users. You can use <code>/count short</code> for counting only in group chats </td>
  </tr>
  <tr>
    <td><code>/newadmin</code></td>
    <td>Add administror. <code>/newadmin 123456789</code></td>
  </tr>
  <tr>
    <td><code>/stats</code></td>
    <td>Getting information on the number of group and personal chats.</td>
  </tr>
  <tr>
    <td><code>/fullstats</code></td>
    <td>Obtaining information on the number of group and personal chats for the entire time, week and month.</td>
  </tr>
  <tr>
    <td><code>/backup</code></td>
    <td>Sends an archive with copies of databases.</td>
  </tr>
  <tr>
    <td><code>/unban</code></td>
    <td>Unban user by ID. <code>/unban 123456789</code></td>
  </tr>
</table>
<b>RUSSIAN VERSION</b><br>
ERTB – exchange rates telegram bot.<br>
Бот распознает в тексте валюты и суммы, а затем присылает сообщение уже с другими валютами. Пример работающего бота: <a href="https://t.me/exchange_rates_vsk_bot">ERTB</a><br><br>
<b>Пример работы бота</b><br>
Ваше сообщение:<br>
<pre>5 баксов</pre>
Ответ бота:
<pre>🇺🇸5.0 USD

🇪🇺4.13 EUR
🇷🇺365.98 RUB
🇺🇦139.83 UAH</pre><br>
<b>Характеристики бота</b>
<table>
  <tr>
    <th>Языки распознавания текста</th>
    <td>Английский, русский и украинский.</td>
  </tr>
  <tr>
    <th>Языки интерфейса бота</th>
    <td>Английский, русский и украинский.</td>
  </tr>
  <tr>
    <th>Распознавание и конвертация классических валют</th>
    <td>161 классическая валюта, а также золото и серебро (в унициях).</td>
  </tr>
  <tr>
    <th>Улучшенное распознавание валют</th>
    <td>29 классических валюта, а также золото и серебро (в унициях).</td>
  </tr>
  <tr>
    <th>Распознавание и конвертация криптовалют</th>
    <td>ADA, BCH, BNB, BTC, DASH, DOGE, ETC, ETH, LTC, RVN, TRX, XLM, XMR, XRP.</td>
  </tr>
  <tr>
    <th>Улучшенное распознавание криптовалют</th>
    <td>Для всех криптовалют, но только на русском и английском.</td>
  </tr>
  <tr>
    <th>API классических валют</th>
    <td><a href="http://data.fixer.io/api/">Fixer.io</a></td>
  </tr>
  <tr>
    <th>API классических валют</th>
    <td><a href="https://api.binance.com/api/v3/">Binance.com</a></td>
  </tr>
</table><br>

<b>Запуск бота</b><br>
По умолчанию бот запускается вот так: <pre>python3 ERTB.py</pre> Также можно включить логирование сообщений и ошибок в терминал: <pre>python3 ERTB.py -l on</pre> или<br><br><pre>python3 ERTB.py --logs on</pre><br>
Ниже приведены все аргументы для запуска:
<table>
  <tr>
    <th>Название</th>
    <th>Аргумент</th>
    <th>Значение</th>
    <th>Пример</th>
    <th>По умолчанию</th>
  </tr>
  <tr>
    <td>Логирование сообщений и ошибок в терминал</td>
    <td><code>--logs</code> или <code>-l</code></td>
    <td><code>on</code> или <code>off</code></td>
    <td><code>python3 ERTB.py --logs on</code></td>
    <td><code>off</code></td>
  </tr>
  <tr>
    <td>Добавление администратора для бота</td>
    <td><code>--admin</code> или <code>-a</code></td>
    <td>ID пользователя</td>
    <td><code>python3 ERTB.py --admin 123456789</code></td>
    <td>отсутствует</td>
  </tr>
  <tr>
    <td>Обработка полученых сообщений при включение</td>
    <td><code>--updates</code> или <code>-u</code></td>
    <td><code>on</code> или <code>off</code></td>
    <td><code>python3 ERTB.py --updates on</code></td>
    <td><code>off</code></td>
  </tr>
</table><br>
<b>Список команд в Телеграме для рядового пользователя</b><br><br>
<table>
  <tr>
    <th>Комманда</th>
    <th>Описание команды</th>
  </tr>
  <tr>
    <td><code>/about</code></td>
    <td>Краткая информация про авторов, версию, исходный код и/или лицензию.</td>
  </tr>
  <tr>
    <td><code>/help</code></td>
    <td>Помощь в использовании и настройки бота.</td>
  </tr>
  <tr>
    <td><code>/settings</code></td>
    <td>Тут можно настроить бота для вашего чата.</td>
  </tr>
  <tr>
    <td><code>/donate</code></td>
    <td>Вы можете поддержать разработку бота чеканной монетой.</td>
  </tr>
  <tr>
    <td><code>/wrong</code></td>
    <td>Ответьте на сообщение, которое бот неправильно распознал данной командой.</td>
  </tr>
</table><br>
<b>Список команд в Телеграме для разработчиков/администраторов</b><br><br>
<table>
  <tr>
    <th>Комманда</th>
    <th>Описание команды</th>
  </tr>
  <tr>
    <td><code>/echo</code></td>
    <td>Рассылка сообщения по всем чатам. После команды нужно написать текст, который желаете разослать.</td>
  </tr>
  <tr>
    <td><code>/count</code></td>
    <td>Получение информации про количество пользователей бота. Можно написать <code>/count short</code> и подсчёт произойдёт только по групповым чатам.</td>
  </tr>
  <tr>
    <td><code>/newadmin</code></td>
    <td>Добавить администратора. <code>/newadmin 123456789</code></td>
  </tr>
  <tr>
    <td><code>/stats</code></td>
    <td>Получение информации по количеству чатов групповых и личных.</td>
  </tr>
  <tr>
    <td><code>/fullstats</code></td>
    <td>Получение информации по количеству чатов групповых и личных за всё время, неделю и месяц.</td>
  </tr>
  <tr>
    <td><code>/backup</code></td>
    <td>Присылает архив с копиями баз данных.</td>
  </tr>
  <tr>
    <td><code>/unban</code></td>
    <td>Разбанить пользователя по ID. <code>/unban 123456789</code></td>
  </tr>
</table>

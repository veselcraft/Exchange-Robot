# Exchange-Robot
<a href="README_RU.md">На русском</a><br>
Exchange-Robot – exchange rates telegram bot that searchs for currencies in your messages and converct it to multiple currencies. Funny fork of original ERTB to hide political things :D<br>
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

## All arguments to run
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

## List of commands for regular user
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

## List of commands in Telegram for developers/administrators
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

## Requirements
<ul>
  <li>Python 3.7+ (Recommended 3.8.10)</li>
  <li>Aiogram 2.14+</li>
  <li>uvloop (may not be supported in Windows)</li>
  <li>ujson</li>
  <li>cchardet</li>
  <li>aiodns</li>
  <li>aiohttp[speedups]</li>
  <li>Numberize 1.0.1</li>
  <li>Requests 2.26.0</li>
</ul>
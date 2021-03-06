
 Windows
git for windows
Цели
Полная готовность к работе с Git.
01Установка имени и электронной почты
Если вы никогда ранее не использовали git, для начала вам необходимо осуществить установку. Выполните следующие команды, чтобы git узнал ваше имя и электронную почту. Если git уже установлен, можете переходить к разделу окончания строк.
ВЫПОЛНИТЬ:
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"
02Параметры установки окончаний строк
Также, для пользователей Unix/Mac:
ВЫПОЛНИТЬ:
git config --global core.autocrlf input
git config --global core.safecrlf true
Для пользователейWindows:
ВЫПОЛНИТЬ:
git config --global core.autocrlf true
git config --global core.safecrlf true
 2. Финальные приготовления
Цели
Установить материалы учебника и подготовить их к работе.
01Скачайте учебные материалы
Скачайте учебные материалы здесь:
http://githowto.com/git_tutorial.zip
02Распакуйте учебные материалы
Пакет учебных материалов должен иметь главную папку «git_tutorial» с двумя подпапками:
work — пустой рабочий каталог. Здесь будут лежать ваши репозитории.
files — заранее упакованные файлы для того, чтобы вы могли продолжить работать с учебными материалами на любом этапе. Если вы застрянете, просто скопируйте нужный урок в свою рабочую папку.
3. Создание проекта
Цели
Научиться создавать git репозиторий с нуля.
01Создайте страницу «Hello, World»
Начните работу в пустом рабочем каталоге (например Work, если вы скачали архив с предыдущего шага) с создания пустого каталога с именем «hello», затем войдите внего и создайте там файл с именем hello.html с таким содержанием.
ВЫПОЛНИТЕ:
mkdir hello
cd hello
touch hello.html
ФАЙЛ: hello.html
Hello, World
02Создайте репозиторий
Теперь у вас есть каталог с одним файлом. Чтобы создать git репозиторий из этого каталога, выполните команду git init.
ВЫПОЛНИТЕ:
git init
РЕЗУЛЬТАТ:
$ git init
Initialized empty Git repository in /Users/alex/Documents/Presentations/githowto/auto/hello/.git/


03Добавьте страницу в репозиторий
Теперь давайте добавим в репозиторий страницу «Hello, World».
ВЫПОЛНИТЕ:
git add hello.html
git commit -m "First Commit"
Вы увидите …
РЕЗУЛЬТАТ:
$ git add hello.html
$ git commit -m "First Commit"
[master (root-commit) 911e8c9] First Commit
 1 files changed, 1 insertions(+), 0 deletions(-)
 create mode 100644 hello.html
4. Проверка состояния
Цели
Научиться проверять состояние репозитория
01Проверьте состояние репозитория
Используйте команду git status, чтобы проверить текущее состояние репозитория.
ВЫПОЛНИТЕ:
git status
Вы увидите
РЕЗУЛЬТАТ:
$ git status
# On branch master
nothing to commit (working directory clean)
Команда проверки состояния сообщит, что коммитить нечего. Это означает, что в репозитории хранится текущее состояние рабочего каталога, и нет никаких изменений, ожидающих записи.
Мы будем использовать команду git status, чтобы продолжать отслеживать состояние репозитория и рабочего каталога.


5. Внесение изменений
Цели
Научиться отслеживать состояние рабочего каталога
01Измените страницу «Hello, World»
Добавим кое-какие HTML-теги к нашему приветствию. Измените содержимое файла на:
ФАЙЛ: hello.html
<h1>Hello, World!</h1>
02Проверьте состояние
Теперь проверьте состояние рабочего каталога.
ВЫПОЛНИТЕ:
git status
Вы увидите …
РЕЗУЛЬТАТ:
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   hello.html
#
no changes added to commit (use "git add" and/or "git commit -a")
Первое, что нужно заметить, это то, что git знает, что файл hello.html был изменен, но при этом эти изменения еще не зафиксированы в репозитории.
Также обратите внимание на то, что сообщение о состоянии дает вам подсказку о том, что нужно делать дальше. Если вы хотите добавить эти изменения в репозиторий, используйте команду git add. В противном случае используйте команду git сheckoutдля отмены изменений.
03А далее...
Давайте проиндексируем изменения.
6. Индексация изменений
Цели
Научиться индексировать изменения для последующих коммитов
01Добавьте изменения
Теперь дайте команду git проиндексировать изменения. Проверьте состояние
ВЫПОЛНИТЕ:
git add hello.html
git status
Вы увидите…
РЕЗУЛЬТАТ:
$ git add hello.html
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html
#
Изменения файла hello.html были проиндексированы. Это означает, что git теперь знает об изменении, но изменение пока не перманентно (читай, навсегда) записано в репозиторий. Следующий коммит будет включать в себя проиндексированные изменения.
Если вы решили, что не хотите коммитить изменения, команда состояния напомнит вам о том, что с помощью команды git resetможно снять индексацию этих изменений.
7. Индексация и коммит
Отдельный шаг индексации в git позволяет вам продолжать вносить изменения в рабочий каталог, а затем, в момент, когда вы захотите взаимодействовать с версионным контролем, git позволит записать изменения в малых коммитах, которые фиксируют то, что вы сделали.
Предположим, что вы отредактировали три файла (a.html, b.html, и c.html). Теперь вы хотите закоммитить все изменения, при этом чтобы изменения в a.html и b.html были одним коммитом, в то время как изменения в c.html логически не связаны с первыми двумя файлами и должны идти отдельным коммитом.
В теории, вы можете сделать следующее:
git add a.html
git add b.html
git commit -m "Changes for a and b"
git add c.html
git commit -m "Unrelated change to c"
Разделяя индексацию и коммит, вы имеете возможность с легкостью настроить, что идет в какой коммит.
8. Коммит изменений
Цели
Научиться коммитить изменения в репозиторий
01Закоммитьте изменения
Достаточно об индексации. Давайте сделаем коммит того, что мы проиндексировали, в репозиторий.
Когда вы ранее использовали git commit для коммита первоначальной версии файла hello.html в репозиторий, вы включили метку -m, которая делает комментарий в командной строке. Команда commit позволит вам интерактивно редактировать комментарии для коммита. Теперь давайте это проверим.
Если вы опустите метку -m из командной строки, git перенесет вас в редактор по вашему выбору. Редактор выбирается из следующего списка (в порядке приоритета):
переменная среды GIT_EDITOR
параметр конфигурации core.editor
переменная среды VISUAL
переменная среды EDITOR
У меня переменная EDITOR установлена в emacsclient (доступен для Linux и Mac).
Сделайте коммит сейчас и проверьте состояние.
ВЫПОЛНИТЕ:
git commit
Вы увидите в вашем редакторе:
РЕЗУЛЬТАТ:
|
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html
#
В первой строке введите комментарий: «Added h1 tag». Сохраните файл и выйдите из редактора (для этого в редакторе по-умолчанию (Vim) вам нужно нажать клавишу ESC, ввести :wq и нажать Enter). Вы увидите…
РЕЗУЛЬТАТ:
git commit
Waiting for Emacs...
[master 569aa96] Added h1 tag
 1 files changed, 1 insertions(+), 1 deletions(-)
Строка «Waiting for Emacs…» получена из программы emacsclient, которая посылает файл в запущенную программу emacs и ждет его закрытия. Остальные выходные данные – стандартные коммит-сообщения.
02Проверьте состояние
В конце давайте еще раз проверим состояние.
ВЫПОЛНИТЕ:
git status
Вы увидите…
РЕЗУЛЬТАТ:
$ git status
# On branch master
nothing to commit (working directory clean)
Рабочий каталог чистый, можете продолжить работу.
9. Изменения, а не файлы
Цели
Понять, что git работает с изменениями, а не файлами.
Большинство систем версионного контроля работают с файлами. Вы добавляете файл в версионный контроль, а система отслеживает изменения файла с этого момента.
Git фокусируется на изменениях в файле, а не самом файле. Когда вы осуществляете команду git add file, вы не говорите git добавить файл в репозиторий. Скорее вы говорите, что git надо отметить текущее состояние файла, коммит которого будет произведен позже.
Мы попытаемся исследовать эту разницу в данном уроке.
01Первое изменение: Добавьте стандартные теги страницы
Измените страницу «Hello, World», чтобы она содержала стандартные теги <html> и <body>.
ФАЙЛ: hello.html
<html>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
02Добавьте это изменение
Теперь добавьте это изменение в индекс git.
ВЫПОЛНИТЕ:
git add hello.html
03Второе изменение: Добавьте заголовки HTML
Теперь добавьте заголовки HTML (секцию <head>) к странице «Hello, World».
ФАЙЛ: hello.html
<html>
  <head>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
04Проверьте текущий статус
ВЫПОЛНИТЕ:
git status
Вы увидите…
РЕЗУЛЬТАТ:
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html
#
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   hello.html
#
Обратите внимание на то, что hello.html указан дважды в состоянии. Первое изменение (добавление стандартных тегов) проиндексировано и готово к коммиту. Второе изменение (добавление заголовков HTML) является непроиндексированным. Если бы вы делали коммит сейчас, заголовки не были бы сохранены в репозиторий.
Давайте проверим.
05Коммит
Произведите коммит проиндексированного изменения (значение по умолчанию), а затем еще раз проверьте состояние.
ВЫПОЛНИТЕ:
git commit -m "Added standard HTML page tags"
git status
Вы увидите…
РЕЗУЛЬТАТ:
$ git commit -m "Added standard HTML page tags"
[master 8c32287] Added standard HTML page tags
 1 files changed, 3 insertions(+), 1 deletions(-)
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   hello.html
#
no changes added to commit (use "git add" and/or "git commit -a")
Состояние команды говорит о том, что hello.html имеет незафиксированные изменения, но уже не в буферной зоне.
06Добавьте второе изменение
Теперь добавьте второе изменение в индекс, а затем проверьте состояние с помощью команды git status.
ВЫПОЛНИТЕ:
git add .
git status
Примечание: В качестве файла для добавления, мы использовали текущий каталог («.»). Это самый краткий и удобный путь для добавления всех изменений в файлы текущего каталога и его подкаталоги. Но поскольку он добавляет все, не лишним будет проверить состояние перед запуском add, просто чтобы убедиться, что вы не добавили какой-то файл, который добавлять было не нужно.
Я хотел показать вам трюк с add, далее мы будем на всякий случай продолжать добавлять явные файлы.
Вы увидите…
РЕЗУЛЬТАТ:
$ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#   modified:   hello.html
#
Второе изменение было проиндексировано и готово к коммиту.
07Сделайте коммит второго изменения
ВЫПОЛНИТЕ:
git commit -m "Added HTML header"
10. История
Цели
Научиться просматривать историю проекта.
Получение списка произведенных изменений — функция команды git log.
ВЫПОЛНИТЕ:
git log
Вы увидите…
РЕЗУЛЬТАТ:
$ git log
commit fa3c1411aa09441695a9e645d4371e8d749da1dc
Author: Alexander Shvets <alex@githowto.com>
Date:   Wed Mar 9 10:27:54 2011 -0500

    Added HTML header

commit 8c3228730ed03116815a5cc682e8105e7d981928
Author: Alexander Shvets <alex@githowto.com>
Date:   Wed Mar 9 10:27:54 2011 -0500

    Added standard HTML page tags

commit 43628f779cb333dd30d78186499f93638107f70b
Author: Alexander Shvets <alex@githowto.com>
Date:   Wed Mar 9 10:27:54 2011 -0500

    Added h1 tag

commit 911e8c91caeab8d30ad16d56746cbd6eef72dc4c
Author: Alexander Shvets <alex@githowto.com>
Date:   Wed Mar 9 10:27:54 2011 -0500

    First Commit
Вот список всех четырех коммитов в репозиторий, которые мы успели совершить.
01Однострочная история
Вы полностью контролируете то, что отображает log. Мне, например, нравится однострочный формат:
ВЫПОЛНИТЕ:
git log --pretty=oneline
Вы увидите…
РЕЗУЛЬТАТ:
$ git log --pretty=oneline
fa3c1411aa09441695a9e645d4371e8d749da1dc Added HTML header
8c3228730ed03116815a5cc682e8105e7d981928 Added standard HTML page tags
43628f779cb333dd30d78186499f93638107f70b Added h1 tag
911e8c91caeab8d30ad16d56746cbd6eef72dc4c First Commit
02Контроль отображения записей
Есть много вариантов выбора, какие элементы отображаются в логе. Поиграйте со следующими параметрами:
git log --pretty=oneline --max-count=2
git log --pretty=oneline --since='5 minutes ago'
git log --pretty=oneline --until='5 minutes ago'
git log --pretty=oneline --author=<your name>
git log --pretty=oneline --all
В unix-системах доступна справочная страница man git log.
03Изощряемся
Вот что я использую для просмотра изменений, сделанных за последнюю неделю. Я добавлю --author=alex, если я хочу увидеть только изменения, которые сделал я.
git log --all --pretty=format:"%h %cd %s (%an)" --since='7 days ago'
04Конечный формат лога
Со временем, я решил, что для большей части моей работы мне подходит следующий формат лога.
ВЫПОЛНИТЕ:
git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
Выглядит это примерно так:
РЕЗУЛЬТАТ:
$ git log --pretty=format:"%h %ad | %s%d [%an]" --graph --date=short
* fa3c141 2011-03-09 | Added HTML header (HEAD, master) [Alexander Shvets]
* 8c32287 2011-03-09 | Added standard HTML page tags [Alexander Shvets]
* 43628f7 2011-03-09 | Added h1 tag [Alexander Shvets]
* 911e8c9 2011-03-09 | First Commit [Alexander Shvets]
Давайте рассмотрим его в деталях:
--pretty="..." — определяет формат вывода.
%h — укороченный хэш коммита
%d — дополнения коммита («головы» веток или теги)
%ad — дата коммита
%s — комментарий
%an — имя автора
--graph — отображает дерево коммитов в виде ASCII-графика
--date=short — сохраняет формат даты коротким и симпатичным
Таким образом, каждый раз, когда вы захотите посмотреть лог, вам придется много печатать. К счастью, мы узнаем о git алиасах в следующем уроке.
05Другие инструменты
Оба gitx (для Mac) и gitk (для любой платформы) полезны в изучении истории изменений.

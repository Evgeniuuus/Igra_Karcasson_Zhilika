Внимат(ш)(ч)но пожалуйста! Правила: https://www.igroved.ru/rules/rules_carcasson-classic_rus.pdf Нужно будет докачать библиотеки из самого pyCharm. Пригодится: pip install pygame-menu

А вообще, чтобы вам голову не греть, я изучил статическую линковку (две команды ниже).

pip install pyinstaller pyinstaller --onefile --noconsole main.py

EXE-шник с текстурами лежит в папке dist (Запускаете и играете)

Управление в программе: -ЛКМ ставить карточки -ПКМ перевернуть карточки

Техника программирования называется САИД. (Стыбзил, Адаптируешь, Используешь, Делишься)

==============================================================================================================================================
                                                    ОБНОВЛЕНИЕ!!!
==============================================================================================================================================
Каркассон теперь с музыкой! (Музыка взята из Warcraft III)

Так как я тефтелька, я не смог запушить старый репозиторий, поэтому создал новый проект в новый репозиторий.

Ссылка конечно же останется такой же. Она все равно должна перекидывать сюда

Также усовершенствованная статическая линковка!

pyinstaller --onefile --noconsole --icon=myicon.ico --add-data "background_music.mp3;." main.py

Наслаждайтесь)))

==============================================================================================================================================
                                                    еще ОБНОВЛЕНИЕ!!!
==============================================================================================================================================

Теперь в два раза больше тайлов, а соответственно в два раза больше веселья)

Скоро будет отдельно меню для выбора количества тайлов и обработка клавиши ESC чтобы программа не была похожа на вирус

А вот дополнение с рекой делать я наверное не стану, там нужно пол программы перелопатить чтобы это сработало. 
С другой стороны можно описать тайлы которых нет в основной игре чтобы повысить мобильность их расстановки, но это как-нибудь потом...
Спасибо за вниматошность)

==============================================================================================================================================

Добавил таки меню выбора количества тайлов вместо обычной кнопки играть

Да еще я не смог сделать плейлист из множества музычек, пришлось склеить в одну, ну разницы нет особо)

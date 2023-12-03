Этот код Python представляет собой сканер сетевых портов. Это позволяет проверить доступность TCP-портов на одной или нескольких целях.

При запуске сценария пользователю предлагается ввести цели (это может быть один IP-адрес или список, разделенный запятыми) и количество портов, которые они хотят сканировать.

Код использует сокеты, чтобы попытаться установить TCP-соединение на каждом из портов, указанных в предоставленных целях. Если соединение установлено успешно, то есть если порт открыт и принимает соединения, на экране отображается сообщение о том, что порт открыт.

Важно отметить, что этот скрипт только проверяет доступность портов, он не выполняет никакого взаимодействия со службами или приложениями, которые могут прослушивать эти порты. Он предоставляет обзор доступности портов, который может быть полезен сетевым администраторам или для базовой диагностики подключения.

Однако крайне важно использовать этот тип инструмента этично и в соответствии с политиками безопасности, получив соответствующее разрешение перед выполнением сканирования портов в системах или сетях, которыми вы не владеете или не авторизуетесь.
![image](https://github.com/kyetav/dvernoy-skaner/assets/132962926/f31684d6-e9e7-4489-b07e-62584dbddae2)

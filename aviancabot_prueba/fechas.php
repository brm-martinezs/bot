<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="viewport" content="width=device-width, initial-scale=1" />

<title>Avianca</title>

<link rel="stylesheet" href="css/demo.css">
<link rel="stylesheet" href="css/form-mini.css">
<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.1/themes/base/jquery-ui.css" />
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.1/jquery-ui.js"></script>

</head>

<body>
	<ul>
        <li>Reporte Escalamiento Grupos Telegram </li>
    </ul>

    <div class="main-content">

        <!-- You only need this form and the form-mini.css -->

        <div class="form-mini-container">

            <form class="form-mini" name="excel" id="excel" method="post" action="generarExcel.php" target="_blank">

                <div class="form-row">
                    <input type="text" id="from" name="from" placeholder="Desde" />
                </div>

                <div class="form-row">
                    <input type="text" id="to" name="to" placeholder="Hasta" />
                </div>


                

                <div class="form-row form-last-row">
                    <input type="submit" name="consultar" value="Consultar">
                </div>

            </form>
        </div>

    </div>

    <script type="text/javascript" src="js/validar.js"></script>

</body>
</html>
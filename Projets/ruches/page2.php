<?php
  $username='root';
  $password = '';
  $servername = 'localhost';
  $db = new PDO('mysql:host=localhost;dbname=ruche2', $username,$password);

?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>ruches</title>
  <link rel="stylesheet" type="text/css" href="style2.css">
  <script type="text/javascript" src="graph.js"></script>
  <link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
<script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" data-auto-replace-svg="nest"></script>

<?php
session_start();
if ($_SESSION['username'] == ""){
	header('Location:index.php');
    
}

?>


</head>
<header>
  <div class="r">
<h1>RUCHES:</h1>
</div>
</header>



<div class="mbox">

<?php

//Requpête SQL pour compter le nombre de ruche.
//et intéhgrer à la place de <9 <$comptage
$cmpt=$db->query("SELECT COUNT(ruche) FROM valeurs")->fetch();
$c=$cmpt[0]+1;

for ($i=1;$i<$c;$i++)
{
$r1="SELECT humidite FROM valeurs WHERE ruche=".$i;
$r2="SELECT temperature FROM valeurs WHERE ruche=".$i;
$r3="SELECT poid FROM valeurs WHERE ruche=".$i;
$hum= $db->query($r1)->fetch();
$temp= $db->query($r2)->fetch();
$poid= $db->query($r3)->fetch();
echo("<div class=\"box\">");
echo("<h2>Ruche".$i."</h2>");
echo("<h3 class=\"tem\">temperature</h3>");
echo ("<h4>".$temp[0]."°C</h4>");
echo("<h3 class=\"hum\">humidité</h3>");
echo("<h4>".$hum[0]."%</h4>");
echo("<h3 class=\"poid\">poid</h3>");
echo("<h4>".$poid[0]."Kg</h4>");
echo ("</div>");
}
?>




</div>

<a href='page2.php?deconnexion=true'><div class="deco"><i class="fas fa-sign-out-alt"></i></div></a>
            
            <?php
                if(isset($_GET['deconnexion']))
                { 
                   if($_GET['deconnexion']==true)
                   {  
                      session_unset();
                      header("location:index.php");
                   }
                }



               
?>

<body>
</body>
</html>

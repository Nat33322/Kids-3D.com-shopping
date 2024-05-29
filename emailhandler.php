<?php
if($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];
  $to = 'njflock11@gmail.com';
  $subject = 'New message from your website';
  
  $headers = "From: " . $email;
  
  mail($to, $subject, $message, $headers);
  echo "Email sent!";
}
?>

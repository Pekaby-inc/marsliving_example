<?php

require 'con/request.php';

$request = new request($_SERVER['REQUEST_URI'], $_GET);
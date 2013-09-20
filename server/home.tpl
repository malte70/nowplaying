<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>{{!title}}</title>
		<meta name="author" content="Malte Bublitz">
		<meta name="generator" content="malte70's NowPlying">
		<meta name="robots" content="noindex">
		<link rel="stylesheet" href="http://malte70.de/img/favicon.png">
		<link rel="stylesheet" href="http://malte70.de/css/bootstrap.min.css">
		<link rel="stylesheet" href="http://malte70.de/css/style.css">
		<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
		<!--[if lt IE 9]>
			<script src="http://malte70.de/js/html5shiv.js"></script>
			<script src="http://malte70.de/js/respond.min.js"></script>
		<![endif]-->
	</head>
	<body>
		<div class="container">
			<div class="header">
				<ul class="nav nav-pills pull-right">
					<li><a href="http://malte70.de">malte70</a></li>
					<li class="active"><a href="/">np</a></li>
				</ul>
				<h3 class="text-muted">malte70 <small>#NowPlaying</small></h3>
			</div>
			<div class="jumbotron">
				<h1>#NowPlaying</h1>
				<p class="lead">{{!current}}</p>
			</div>
			<div class="row marketing jumbotron-bg">
				<div class="col-lg-12">
					<h4>Recently played</h4>
					{{!content}}
				</div>
			</div>
			<div class="footer">
				<p>&copy; <a href="https://malte-bublitz.de">Malte Bublitz</a> 2013 :: <a href="http://malte70.de/impressum/">Impressum</a></p>
			</div>
		</div>
		<script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
		<script src="http://malte70.de/js/bootstrap.min.js"></script>
	</body>
</html>

<script>
	import '../app.pcss';
</script>

<nav
	class="container fixed left-0 right-0 top-0 mx-auto flex h-20 items-center bg-white/70 px-20 backdrop-blur-md"
>
	<div class="flex w-full items-center justify-between">
		<a href="/" class="font-bold">DRUG ADDICTION DETECTION</a>
	</div>
</nav>
<section class="flex min-h-screen w-full flex-col">
	<main class="container mx-auto flex-1 px-20 pt-20">
		<slot></slot>
	</main>
	<footer class="flex items-center justify-center">
		<div class="max-w-4xl py-10 text-center text-sm">
			It is important to remember that this program is not intended to diagnose or treat addiction.
			If you are concerned about your own or someone else's addiction, please reach out to a
			qualified healthcare provider or mental health professional for proper diagnosis, treatment,
			and support.
		</div>
	</footer>
</section>

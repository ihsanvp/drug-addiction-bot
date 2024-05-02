<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import type { PageData } from './$types';

	export let data: PageData;

	// const showMap = data.stage.name == 'Stage 4';
	const showMap = true;
</script>

<div class="flex flex-col items-center justify-center py-10">
	<h1 class="text-6xl font-medium capitalize">Result</h1>
	<h2 class="mt-20 text-4xl font-medium capitalize">{data.stage.name} ({data.stage.desc})</h2>
	<h3 class="mt-10 text-2xl">Solutions</h3>
	<div class="mt-5 flex gap-5">
		{#each data.solutions as solution}
			<Button variant="secondary">{solution}</Button>
		{/each}
	</div>
	{#if showMap}
		<div class="mt-5">
			<iframe
				title="location"
				src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3916.714226438932!2d76.22139831125547!3d10.984929589131623!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3ba7ccfe1700500f%3A0x8b563522c4a15a25!2sAl%20Shifa%20Hospital%20Rd%2C%20Valiyangadi%2C%20Perinthalmanna%2C%20Kerala%20679322!5e0!3m2!1sen!2sin!4v1714671544984!5m2!1sen!2sin"
				width="600"
				height="450"
				style="border:0;"
				loading="lazy"
				referrerpolicy="no-referrer-when-downgrade"
				allowfullscreen
			></iframe>
		</div>
	{/if}
</div>

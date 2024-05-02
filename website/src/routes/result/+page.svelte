<script lang="ts">
	import { Button } from '$lib/components/ui/button';
	import type { PageData } from './$types';

	export let data: PageData;
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
</div>

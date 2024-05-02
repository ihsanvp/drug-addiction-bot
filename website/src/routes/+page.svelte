<script>
	import Button from '$lib/components/ui/button/button.svelte';
	import * as Card from '$lib/components/ui/card';
</script>

<div class="flex items-center justify-center py-20">
	<Card.Root class="w-full">
		<Card.Header>
			<Card.Title class="text-center text-4xl font-bold"
				>Are You worried about yourself or your loved one?</Card.Title
			>
		</Card.Header>
		<Card.Footer class="mt-5 flex items-center justify-center gap-5">
			<Button href="/assessment/myself" class="w-40" color="primary">Myself</Button>
			<Button href="/assessment/loved-one" class="w-40" color="primary">Loved One</Button>
		</Card.Footer>
	</Card.Root>
</div>

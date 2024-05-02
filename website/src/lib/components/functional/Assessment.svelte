<script lang="ts">
	import * as Tabs from '$lib/components/ui/tabs';
	import * as Card from '$lib/components/ui/card';
	import * as RadioGroup from '$lib/components/ui/radio-group';
	import { Label } from '$lib/components/ui/label';
	import { CircleCheck } from 'lucide-svelte';
	import { Button } from '../ui/button';
	import { createEventDispatcher } from 'svelte';

	type Question = {
		name: string;
		question: string;
		options: Array<{
			label: string;
			value: string;
		}>;
		handler?: (answer: string) => Promise<void> | void;
	};

	export let questions: Question[];

	const dispatch = createEventDispatcher();
	const keys = questions.map((q) => q.name);

	let answers: Array<undefined | string> = questions.map((q) => undefined);
	let key: number = 0;

	function onOptionChange(index: number, value: string) {
		answers = [
			...answers.map((v, i) => {
				if (index == i) {
					return value;
				}
				return v;
			})
		];
	}

	async function onNext() {
		console.log(key, questions.length);
		const question = questions[key];
		const answer = answers[key];

		if (question.handler && answer) {
			await question.handler(answer.split('--').reverse()[0]);
		}

		if (answer) {
			if (key < questions.length - 1) {
				key += 1;
			}
			if (key == questions.length - 1) {
				const finalAnswers = answers.map((a) => a?.split('--').reverse()[0]);
				const result = questions.map((q, i) => ({
					name: q.name,
					question: q.question,
					answer: finalAnswers[i]
				}));
				dispatch('complete', result);
			}
		}
	}
</script>

<Tabs.Root value={keys[key]} class="flex w-full flex-row gap-5" orientation="vertical">
	<Tabs.List class="flex h-full flex-col gap-3">
		{#each questions as question, i}
			{@const isDone = i < key}
			<div
				class="flex w-full min-w-32 items-center justify-between rounded-md bg-white px-3 py-2 text-sm"
				class:active={keys[key] == question.name}
				class:done={isDone}
			>
				<span>{question.name}</span>
				{#if isDone}
					<CircleCheck />
				{/if}
			</div>
		{/each}
	</Tabs.List>
	{#each questions as question, idx}
		<Tabs.Content class="m-0 w-full" value={question.name}>
			<Card.Root>
				<Card.Header>
					<Card.Title class="text-center text-4xl font-medium">{question.question}</Card.Title>
				</Card.Header>
				<Card.Content>
					<RadioGroup.Root
						value={answers[key]}
						onValueChange={(value) => onOptionChange(idx, value)}
					>
						{#each question.options as option}
							<div
								class="bg-primary-foreground hover:bg-primary hover:text-primary-foreground group flex items-center rounded-md"
							>
								<RadioGroup.Item
									class="group-hover:border-secondary group-hover:text-secondary ml-5"
									value={`${question.name.split(' ').join('-')}--${option.value}`}
									id={`${question.name.split(' ').join('-')}--${option.value}`}
								/>
								<Label
									class="w-full cursor-pointer px-5 py-4"
									for={`${question.name.split(' ').join('-')}--${option.value}`}
									>{option.label}</Label
								>
							</div>
						{/each}
					</RadioGroup.Root>
				</Card.Content>
				<Card.Footer class="flex items-center justify-center">
					<Button disabled={answers[key] == undefined} on:click={onNext}>
						{key == questions.length - 1 ? 'Submit' : 'Next'}
					</Button>
				</Card.Footer>
			</Card.Root>
		</Tabs.Content>
	{/each}
</Tabs.Root>

<style>
	.active {
		@apply bg-primary text-primary-foreground;
	}
	.done {
		@apply bg-green-500 text-white;
	}
</style>

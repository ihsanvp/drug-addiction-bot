<script lang="ts">
	import { goto } from '$app/navigation';
	import { apiClient } from '$lib/api';
	import Assessment from '$lib/components/functional/Assessment.svelte';

	async function onAssessmentComplete(
		e: CustomEvent<Array<{ name: string; question: String; answer: string }>>
	) {
		const answers = e.detail.filter((r) => r.name.includes('Question')).map((r) => r.answer);
		const {
			data: { stage }
		} = await apiClient.post<{ stage: string }>('/detect-stage', { answers });

		const params = new URLSearchParams();
		params.append('stage', stage);
		goto('/result' + '?' + params.toString());
	}
</script>

<div class="flex items-center justify-center py-20">
	<Assessment
		on:complete={onAssessmentComplete}
		questions={[
			{
				name: 'Phase 1',
				question: 'Have you used any type of drugs?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				],
				handler: async (answer) => {
					if (answer == 'no') {
						await goto('/appreciation/no-drugs');
					}
				}
			},
			{
				name: 'Phase 2',
				question: 'Was it your first time?',
				options: [
					{
						label: 'First time',
						value: 'firsttime'
					},
					{
						label: 'Not first time',
						value: 'notfirsttime'
					}
				],
				handler: async (answer) => {
					if (answer == 'firsttime') {
						await goto('/appreciation/first-time');
					}
				}
			},
			{
				name: 'Question 1',
				question:
					'Do you often use drugs or alcohol in larger amounts or over a longer period of time than you intended?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 2',
				question:
					'Have you for a while now wanted to cut back on drugs or alcohol or made unsuccessful attempts to do so?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 3',
				question:
					'Do you spend a great deal of time finding, using, or recovering from drugs or alcohol?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 4',
				question: 'Do you have strong urges or powerful cravings to use drugs or alcohol?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 5',
				question:
					'Has your use of drugs or alcohol resulted in your inability to meet your obligations at work, home, or school?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 6',
				question:
					'Have you had to cut back on or abandon social, professional, or recreational activities due to your use of drugs or alcohol?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 7',
				question:
					'Have you repeatedly used drugs or alcohol when it was hazardous to do so, such as while driving a car or operating machinery?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 8',
				question:
					'Have you experienced social or relationship problems due to your use of drugs or alcohol and kept using anyway?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 9',
				question:
					'Have you kept using drugs or alcohol knowing that it has caused or worsened physical or mental health issues?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 10',
				question:
					'When you attempt to cut back on or stop your use of drugs or alcohol, have you experienced uncomfortable physical or mental health symptoms (withdrawal)?',
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			},
			{
				name: 'Question 11',
				question:
					"Have you experienced diminished effects when you use drugs or alcohol compared to the past and/or have you needed more drugs or alcohol in order to feel the effects you're seeking (tolerance)?",
				options: [
					{
						label: 'Yes',
						value: 'yes'
					},
					{
						label: 'No',
						value: 'no'
					}
				]
			}
		]}
	/>
</div>

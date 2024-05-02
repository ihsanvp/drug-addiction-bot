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
				question: 'Have they used any type of drugs?',
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
				question: 'Was it their first time?',
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
					'Do they often use drugs or alcohol in larger amounts or over a longer period of time than they intended?',
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
					'Have they for a while now wanted to cut back on drugs or alcohol or made unsuccessful attempts to do so?',
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
					'Do they spend a great deal of time finding, using, or recovering from drugs or alcohol?',
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
				question: 'Do they have strong urges or powerful cravings to use drugs or alcohol?',
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
					'Has their use of drugs or alcohol resulted in their inability to meet their obligations at work, home, or school?',
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
					'Have they had to cut back on or abandon social, professional, or recreational activities due to their use of drugs or alcohol?',
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
					'Have they repeatedly used drugs or alcohol when it was hazardous to do so, such as while driving a car or operating machinery?',
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
					'Have they experienced social or relationship problems due to their use of drugs or alcohol and kept using anyway?',
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
					'Have they kept using drugs or alcohol knowing that it has caused or worsened physical or mental health issues?',
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
					'When they attempt to cut back on or stop their use of drugs or alcohol, have they experienced uncomfortable physical or mental health symptoms (withdrawal)?',
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
					"Have they experienced diminished effects when they use drugs or alcohol compared to the past and/or have they needed more drugs or alcohol in order to feel the effects you're seeking (tolerance)?",
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

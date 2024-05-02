import { apiClient } from '$lib/api';
import { error } from '@sveltejs/kit';

/** @type {import("./$types").PageLoad} */
export async function load({ url }) {
	const stage = url.searchParams.get('stage');
	if (!stage) {
		return error(400, 'Invalid stage');
	}
	const { data: stageData, status } = await apiClient.post<{ stage: string; name: string }>(
		'/stage',
		{ stage }
	);
	if (status != 200) {
		return error(400, 'Invalid stage');
	}
	const { data: solutionsData } = await apiClient.post<{ solutions: string[] }>(
		'/recommend-solutions',
		{ stage: stageData.stage }
	);

	return {
		stage: {
			name: stageData.stage,
			desc: stageData.name
		},
		solutions: solutionsData.solutions
	};
}

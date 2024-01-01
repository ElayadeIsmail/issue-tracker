import { BaseHeader } from '~/components/BaseHeader';

import type { RouteDefinition, RouteSectionProps } from '@solidjs/router';
export const route = {
	load() {
		// define load function
	},
} satisfies RouteDefinition;
export default function HomeLayout(props: RouteSectionProps) {
	return (
		<>
			<BaseHeader />
			{props.children}
		</>
	);
}

import { RouteSectionProps } from '@solidjs/router';

const AuthLayout = (props: RouteSectionProps) => {
	return <div>{props.children}</div>;
};

export default AuthLayout;

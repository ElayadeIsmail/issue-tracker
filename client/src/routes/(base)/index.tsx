import MySiteTitle from '~/components/SiteTitle';

export default function Index() {
	return (
		<>
			<MySiteTitle>Home</MySiteTitle>
			<main class='h-[calc(100vh-64px)] max-w-5xl container flex justify-center'>
				<span class='text-center text-primary font-medium  mx-auto text-sm italic mt-4'>
					Track Your Project Issues
				</span>
			</main>
		</>
	);
}

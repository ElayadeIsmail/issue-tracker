import MySiteTitle from '~/components/SiteTitle';

export default function Index() {
	return (
		<>
			<MySiteTitle>Home</MySiteTitle>
			<main class='h-[calc(100vh-64px)] max-w-5xl container flex items-center justify-center flex-col'>
				<span class='text-center text-primary font-medium text-sm italic mb-4'>
					Track Your Project Issues
				</span>
				<h1 class='text-[5rem] font-bold leading-[5.25rem] text-center'>
					Track And Collaborate <br /> With{' '}
					<span class='text-primary'>Ease</span>
				</h1>
				<p class='text-center text-foreground/60 mt-4'>
					Lorem ipsum dolor sit amet, consectetur adipisicing elit.
					Neque distinctio in illum, repellendus dolorum aperiam optio
					aspernatur cum numquam commodi quaerat id nostrum, error
					debitis aliquam, totam facere voluptate! Architecto!
				</p>
			</main>
		</>
	);
}

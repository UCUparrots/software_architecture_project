/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./app/**/*.{js,ts,jsx,tsx,mdx}',
		'./pages/**/*.{js,ts,jsx,tsx,mdx}',
		'./components/**/*.{js,ts,jsx,tsx,mdx}',
	],
	theme: {
		extend: {
			backgroundImage: {
				'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
				'gradient-conic':
					'conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))',
			},
		},
		colors: {
			'primary-dark': '#36185A',
			primary: '#4A148C',
			'primary-light': '#C2A9E0',
			'calendar-gray': '#B9B9B9',
			white: '#F6F6F6',
			'main-black': '#181A1B',
			gray: '#D9D9D9',
			'dark-gray': '#8E8F94',
			stars: '#EBAD35',
			black: '#181A1B',
		},
	},
	plugins: [],
};

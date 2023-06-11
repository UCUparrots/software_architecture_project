import { Inter } from 'next/font/google';
import React, { useState } from 'react';
import LoginPage from './LoginPage';

const inter = Inter({ subsets: ['latin'] });

export default function Home({ children }) {
	return (
		<main>
			<LoginPage />
		</main>
	);
}

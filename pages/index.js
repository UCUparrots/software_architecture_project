import { Inter } from 'next/font/google';
import React, { useState } from 'react';
import DoctorInfoPage from './DoctorInfoPage';

const inter = Inter({ subsets: ['latin'] });

export default function Home({ children }) {
	return (
		<main>
			<DoctorInfoPage />
		</main>
	);
}

import { Inter } from 'next/font/google';
import Sidebar from '@/components/Sidebar';
import React, { useState } from 'react';
import PersonalInfo from '@/components/PersonalInfo';

const inter = Inter({ subsets: ['latin'] });

export default function Home() {
	const [isActive, setIsActive] = useState(false);

	const handleSidebarToggle = (isActive) => {
		setIsActive(isActive);
	};

	return (
		<main
			className='flex min-h-screen flex-col items-center 
			justify-between p-24 relative w-full overflow-hidden bg-white'
		>
			<Sidebar onToggle={handleSidebarToggle} />

			<div
				className={`absolute h-full transition-all duration-500 ease-in-out p-10
				${
					isActive
						? 'left-[240px] w-calc(100% - 240px)'
						: 'left-[78px] w-calc(100% - 78px)'
				}`}
			>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Personal Info
				</h1>
				<PersonalInfo
					name='Steven Holmes'
					descr='Dantist in North Caroline'
					about='Love flowers and money. Some more information to fill in the blank space and mark down that today is a sunny day. All the best.'
					specialization='Dantist: second class'
					phone='(380) 94 254 44 13'
					date='12/03/1983'
					email='stevenHole@leekar.com'
					rate={4}
				/>
			</div>
		</main>
	);
}

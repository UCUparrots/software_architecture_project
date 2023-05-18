import DoctorSchedule from '@/components/DoctorSchedule';
import Layout from '@/components/Layout';
import React from 'react';

function DoctorSchedulePage() {
	return (
		<Layout>
			<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
				Health Card
			</h1>
			<DoctorSchedule />
		</Layout>
	);
}

export default DoctorSchedulePage;

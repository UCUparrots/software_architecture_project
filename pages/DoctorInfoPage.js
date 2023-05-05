import React from 'react';
import DoctorInfo from '@/components/DoctorInfo';
import Layout from '@/components/Layout';

function DoctorInfoPage() {
	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Personal Info
				</h1>
				<DoctorInfo
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
		</Layout>
	);
}

export default DoctorInfoPage;

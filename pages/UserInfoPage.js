import Layout from '@/components/Layout';
import { useContext } from 'react';
import UserInfo from '@/components/UserInfo';
import { MyContext } from '@/AppStateProvider';

function UserInfoPage() {
	const { isDoctor } = useContext(MyContext);

	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					{isDoctor ? 'User Info' : 'My Info'}
				</h1>
				<UserInfo
					name='Ilya Konsty'
					phone='(380) 94 254 44 13'
					date='12/03/1983'
					email='IlyaKonsty@gmail.com'
					residence='Kalynivka, Kyiv district'
				/>
			</div>
		</Layout>
	);
}

export default UserInfoPage;

import Layout from '@/components/Layout';
import { useContext } from 'react';
import UserInfo from '@/components/UserInfo';
import { MyContext } from '@/AppStateProvider';

function UserInfoPage({ info }) {
	const { isDoctor, userId } = useContext(MyContext);

	info = JSON.parse(info);

	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					{isDoctor ? 'User Info' : 'My Info'}
				</h1>
				<UserInfo
					id={userId}
					name={info.firstname + ' ' + info.lastname}
					phone={info.phone}
					date={info.birthdate}
					email={info.email}
				/>
			</div>
		</Layout>
	);
}

export default UserInfoPage;

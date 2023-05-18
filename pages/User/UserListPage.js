import Layout from '@/components/Layout';
import UserList from '@/components/User/UserList';

function UserListPage() {
	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Your patients
				</h1>
				<UserList />
			</div>
		</Layout>
	);
}

export default UserListPage;

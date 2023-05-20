import { useContext } from 'react';
import { MyContext } from '@/AppStateProvider';
import UserInfoPage from './UserInfoPage';
import DoctorInfoPage from './DoctorInfoPage';

function InfoPage() {
	const { isDoctor } = useContext(MyContext);

	return <>{isDoctor ? <DoctorInfoPage /> : <UserInfoPage />};</>;
}

export default InfoPage;

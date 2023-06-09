import { useContext, useEffect, useState } from 'react';
import { MyContext } from '@/AppStateProvider';
import UserInfoPage from './UserInfoPage';
import DoctorInfoPage from './DoctorInfoPage';
import axios from 'axios';

function InfoPage() {
	const { isDoctor, userId } = useContext(MyContext);
	const [answer, setAnswer] = useState(null);

	const getInfo = async () => {
		try {
			const response = await axios.get('/loginS/get_info', {
				params: {
					user_id: userId,
				},
			});

			setAnswer(response.data);
		} catch (error) {
			console.error(error);
		}
	};

	useEffect(() => {
		getInfo();
	}, []);

	if (answer === null) {
		// You can show a loading indicator or return null until the answer is fetched
		return null;
	}

	return (
		<>
			{isDoctor ? (
				<DoctorInfoPage info={answer} />
			) : (
				<UserInfoPage info={answer} />
			)}
			;
		</>
	);
}

export default InfoPage;

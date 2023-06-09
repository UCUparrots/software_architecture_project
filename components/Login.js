import Link from 'next/link';
import { useState, useContext } from 'react';
import { MyContext } from '@/AppStateProvider';
import axios from 'axios';
import { useRouter } from 'next/router';
import { Alert, AlertTitle } from '@mui/material';

function Login() {
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [showWarning, setShowWarning] = useState(false);

	const { isDoctor, setIsDoctor, setUserId } = useContext(MyContext);
	const router = useRouter();

	const handleShowWarning = () => {
		setShowWarning(true);
	};

	const handleCloseWarning = () => {
		setShowWarning(false);
	};

	const handleSubmit = async (event) => {
		event.preventDefault();
		const url = '/loginS/login';
		const data = {
			email: email,
			password_hash: password,
			login_as_doctor: isDoctor,
		};
		const headers = {
			'Content-Type': 'application/json',
		};

		try {
			const response = await axios.post(url, data, { headers });
			// console.log(response.data);
			if (response.data) {
				setUserId(response.data);
				router.push('/InfoPage');
			} else {
				handleShowWarning();
			}
		} catch (error) {
			console.error(error);
		}
	};

	return (
		<div className='bg-white h-[55vh] w-[25vw] rounded-lg flex items-center flex-col justify-center'>
			<div className='text-[60px] mb-6'>Log in</div>
			<form action='' onSubmit={handleSubmit}>
				<div className='text-dark-gray pl-4'>Email</div>
				<div
					className='border-2 rounded-lg border-gray h-[5vh] w-[19vw] 
                focus-within:border-primary px-2 mb-2 transition-all duration-500 ease-in-out'
				>
					<input
						className='h-full bg-white focus:outline-none w-full caret-dark-gray'
						type='email'
						onChange={(e) => setEmail(e.target.value)}
					/>
				</div>
				<div className='text-dark-gray pl-4'>Password</div>
				<div
					className='border-2 rounded-lg border-gray h-[5vh] w-[19vw]
                focus-within:border-primary px-2 transition-all duration-500 ease-in-out'
				>
					<input
						className='h-full bg-white focus:outline-none w-full caret-dark-gray'
						type='password'
						onChange={(e) => setPassword(e.target.value)}
					/>
				</div>
				<div className='mt-2'>
					<input
						type='checkbox'
						id='isDoctor'
						name='isDoctor'
						className='w-4 h-4 mr-3'
						checked={isDoctor}
						onChange={(event) => setIsDoctor(event.target.checked)}
					/>
					<label htmlFor='isDoctor' className='text-dark-gray'>
						Are you a doctor?
					</label>
				</div>

				<div className='text-primary text-sm mt-5 mb-3'>Forgot password?</div>

				<button
					type='submit'
					className='rounded-lg h-[5vh] w-[19vw]
					bg-primary px-2 transition-all duration-500 ease-in-out text-white'
				>
					LOG IN
				</button>
				<div className='flex text-sm mt-7 justify-center'>
					<div>Dont have an account?</div>
					<Link href='/SignupPage' className='text-primary ml-1'>
						Sign up
					</Link>
				</div>
			</form>
			{showWarning && (
				<Alert severity='error' onClose={handleCloseWarning}>
					<AlertTitle>Error</AlertTitle>
					The user does not exist or the password is incorrect
				</Alert>
			)}
		</div>
	);
}

export default Login;

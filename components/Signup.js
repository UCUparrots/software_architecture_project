import Link from 'next/link';
import { useRouter } from 'next/router';
import { useState } from 'react';
import { useContext } from 'react';
import { MyContext } from '@/AppStateProvider';
import { Alert, AlertTitle } from '@mui/material';
import axios from 'axios';

function Signup() {
	const [name, setName] = useState('');
	const [surname, setSurname] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [birth, setBirth] = useState('');
	const [phone, setPhone] = useState('');
	const [wantMsg, setWantMsg] = useState(false);
	const [showWarning, setShowWarning] = useState(false);

	const [page, setPage] = useState(1);

	const router = useRouter();
	const { isDoctor, setIsDoctor, setUserId } = useContext(MyContext);

	const handleShowWarning = () => {
		setShowWarning(true);
	};

	const handleCloseWarning = () => {
		setShowWarning(false);
	};

	const handleSubmit = async (event) => {
		event.preventDefault();
		const url = '/loginS/signup';
		if (
			name.length == 0 ||
			email.length == 0 ||
			password.length == 0 ||
			surname.length == 0 ||
			phone.length == 0 ||
			birth.length == 0
		) {
			handleShowWarning();
		} else {
			const data = {
				email: email,
				password_hash: password,
				firstname: name,
				lastname: surname,
				phone: phone,
				birthdate: birth,
				notification: wantMsg,
				is_doctor: isDoctor,
			};
			const headers = {
				'Content-Type': 'application/json',
			};

			try {
				const response = await axios.post(url, data, { headers });
				if (response.data) {
					setUserId(response.data);
					router.push('/InfoPage');
				}
			} catch (error) {
				console.error(error);
			}
		}
	};

	function handleNext() {
		if (
			name.length == 0 ||
			email.length == 0 ||
			password.length == 0 ||
			surname.length == 0
		) {
			handleShowWarning();
		} else {
			handleCloseWarning();
			setPage(2);
		}
	}

	function handlePrev() {
		setPage(1);
	}

	return (
		<div className='bg-white h-[75vh] w-[25vw] rounded-lg flex items-center flex-col justify-center'>
			<div className='text-[60px] mb-6'>Sign up</div>
			<form action='' onSubmit={handleSubmit}>
				{page === 1 && (
					<>
						<div className='text-dark-gray pl-4'>Name</div>
						<div
							className='border-2 rounded-lg border-gray h-[5vh] w-[19vw] 
						focus-within:border-primary px-2 mb-2 transition-all duration-500 ease-in-out'
						>
							<input
								className='h-full bg-white focus:outline-none w-full caret-dark-gray'
								type='text'
								onChange={(e) => setName(e.target.value)}
							/>
						</div>
						<div className='text-dark-gray pl-4'>Surname</div>
						<div
							className='border-2 rounded-lg border-gray h-[5vh] w-[19vw] 
                focus-within:border-primary px-2 mb-2 transition-all duration-500 ease-in-out'
						>
							<input
								className='h-full bg-white focus:outline-none w-full caret-dark-gray'
								type='text'
								onChange={(e) => setSurname(e.target.value)}
							/>
						</div>
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

						<button
							className='rounded-lg h-[5vh] w-[19vw]
                bg-primary px-2 transition-all duration-500 ease-in-out text-white mt-[6vh]'
							onClick={handleNext}
						>
							NEXT
						</button>

						<div className='flex text-sm mt-7 justify-center'>
							<div>Already have an account?</div>
							<Link href='/LoginPage' className='text-primary ml-1'>
								Log in
							</Link>
						</div>
					</>
				)}

				{page === 2 && (
					<>
						<div className='text-dark-gray pl-4'>Date of birth</div>
						<div
							className='border-2 rounded-lg border-gray h-[5vh] w-[19vw] 
					focus-within:border-primary px-2 mb-2 transition-all duration-500 ease-in-out'
						>
							<input
								className='h-full bg-white focus:outline-none w-full caret-dark-gray'
								type='text'
								onChange={(e) => setBirth(e.target.value)}
							/>
						</div>
						<div className='text-dark-gray pl-4'>Phone number</div>
						<div
							className='border-2 rounded-lg border-gray h-[5vh] w-[19vw] 
			focus-within:border-primary px-2 mb-2 transition-all duration-500 ease-in-out'
						>
							<input
								className='h-full bg-white focus:outline-none w-full caret-dark-gray'
								type='text'
								onChange={(e) => setPhone(e.target.value)}
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
						<div className='mt-2'>
							<input
								type='checkbox'
								id='wantMsg'
								name='wantMsg'
								className='w-4 h-4 mr-3'
								checked={wantMsg}
								onChange={(event) => setWantMsg(event.target.checked)}
							/>
							<label htmlFor='wantMsg' className='text-dark-gray'>
								Do you want to get messages?
							</label>
						</div>

						<button
							type='submit'
							className='rounded-lg h-[5vh] w-[19vw]
			bg-primary px-2 transition-all duration-500 ease-in-out text-white mt-[6vh]'
						>
							SIGN UP
						</button>

						<div className='flex text-sm mt-7 justify-center'>
							<div>Already have an account?</div>
							<Link href='/LoginPage' className='text-primary ml-1'>
								Log in
							</Link>
						</div>
					</>
				)}
			</form>
			{showWarning && (
				<Alert severity='error' onClose={handleCloseWarning}>
					<AlertTitle>Error</AlertTitle>
					Input all fields
				</Alert>
			)}
			<div className='flex mt-8 w-[19vw] justify-end'>
				<div className='text-primary'>{page === 1 ? 1 : 2}</div>
				<div>/2</div>
				{page === 2 ? (
					<button onClick={handlePrev} className='text-primary text-sm ml-1'>
						Prev
					</button>
				) : (
					<></>
				)}
			</div>
		</div>
	);
}

export default Signup;

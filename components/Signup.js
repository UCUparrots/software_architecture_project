import Link from 'next/link';
import { useRouter } from 'next/router';
import { useState } from 'react';
import { useContext } from 'react';
import { MyContext } from '@/AppStateProvider';

function Signup() {
	const [name, setName] = useState('');
	const [surname, setSurname] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [birth, setBirth] = useState('');
	const [residence, setResidence] = useState('');

	const [page, setPage] = useState(1);

	const router = useRouter();
	const { isDoctor, setIsDoctor } = useContext(MyContext);

	const redirect = () => {
		if (isDoctor) {
			router.push('/DoctorInfoPage');
		} else {
			router.push('/UserInfoPage');
		}
	};

	function handleSubmit() {
		const response = {
			name: name,
			surname: surname,
			email: email,
			password: password,
			birth: birth,
			residence: residence,
		};
		console.log(response);
	}

	function handleNext() {
		setPage(2);
	}

	return (
		<div className='bg-white h-[75vh] w-[25vw] rounded-lg flex items-center flex-col justify-center'>
			<div className='text-[60px] mb-6'>Sign up</div>
			<form action='' onSubmit={handleSubmit}>
				{page === 1 ? (
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
							type='submit'
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
				) : (
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
						<div className='text-dark-gray pl-4'>Place of residence</div>
						<div
							className='border-2 rounded-lg border-gray h-[5vh] w-[19vw] 
			focus-within:border-primary px-2 mb-2 transition-all duration-500 ease-in-out'
						>
							<input
								className='h-full bg-white focus:outline-none w-full caret-dark-gray'
								type='text'
								onChange={(e) => setResidence(e.target.value)}
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

						<Link href='/InfoPage'>
							<button
								type='submit'
								className='rounded-lg h-[5vh] w-[19vw]
			bg-primary px-2 transition-all duration-500 ease-in-out text-white mt-[6vh]'
								onClick={redirect}
							>
								SIGN UP
							</button>
						</Link>

						<div className='flex text-sm mt-7 justify-center'>
							<div>Already have an account?</div>
							<Link href='/LoginPage' className='text-primary ml-1'>
								Log in
							</Link>
						</div>
					</>
				)}
			</form>
			<div className='flex mt-8 w-[19vw] justify-end'>
				<div className='text-primary'>{page === 1 ? 1 : 2}</div>
				<div>/2</div>
			</div>
		</div>
	);
}

export default Signup;

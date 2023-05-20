import Link from 'next/link';
import { useState, useContext } from 'react';
import { MyContext } from '@/AppStateProvider';

function Login() {
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');

	const { isDoctor, setIsDoctor } = useContext(MyContext);

	function handleSubmit() {
		const response = {
			email: email,
			password: password,
		};
		console.log(response);
	}

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

				<Link href='/InfoPage'>
					<button
						type='submit'
						className='rounded-lg h-[5vh] w-[19vw]
					bg-primary px-2 transition-all duration-500 ease-in-out text-white'
					>
						LOG IN
					</button>
				</Link>
				<div className='flex text-sm mt-7 justify-center'>
					<div>Dont have an account?</div>
					<Link href='/SignupPage' className='text-primary ml-1'>
						Sign up
					</Link>
				</div>
			</form>
		</div>
	);
}

export default Login;

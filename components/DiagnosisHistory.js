import { useEffect, useState } from 'react';

function DiagnosisHistory() {
	const [diagnosises, setDiagnosises] = useState(null);

	useEffect(() => {
		setDiagnosises([
			{
				id: 0,
				diagnosis: 'One',
				medicine: 'm one',
				startDate: '1/1/1992',
				resolveDate: '1/1/1',
			},
			{
				id: 1,
				diagnosis: 'Two',
				medicine: 'm two',
				startDate: '2/2/2',
				resolveDate: '2/2/2',
			},
			{
				id: 2,
				diagnosis: 'Three',
				medicine: 'm three',
				startDate: '3/3/3',
				resolveDate: '3/3/3',
			},
		]);
	}, []);

	if (diagnosises === null) {
		return <div>Loading...</div>;
	}

	return (
		<div className='w-[30vw] h-[20vh] overflow-auto border border-primary rounded-lg p-1'>
			<ul>
				{diagnosises.map((diagnosis) => (
					<li
						key={diagnosis.id}
						className='h-[10vh] border border-dark-gray rounded-lg mb-1
                        flex justify-between bg-white drop-shadow-md p-2 items-center'
					>
						<div className='text-dark-gray'>
							<div className='mb-5'>Start date: {diagnosis.startDate}</div>
							<div>Resolved date: {diagnosis.resolveDate}</div>
						</div>
						<div>
							<div className='mb-5 flex'>
								<div className='text-primary mr-2'>Diagnosis:</div>
								{diagnosis.diagnosis}
							</div>
							<div className='flex'>
								<div className='text-primary mr-2'>Medicine:</div>
								{diagnosis.medicine}
							</div>
						</div>
					</li>
				))}
			</ul>
		</div>
	);
}

export default DiagnosisHistory;

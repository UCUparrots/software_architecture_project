import Diagnosis from './Diagnosis';

function DiagnosisHistory({ data }) {
	return (
		<div className='w-[30vw] h-[25vh] overflow-auto border border-primary rounded-lg p-1'>
			<ul>
				{data.map((diagnosis) => (
					<Diagnosis key={diagnosis.id} diagnosis={diagnosis} />
				))}
			</ul>
		</div>
	);
}

export default DiagnosisHistory;

import type { EchoResponse } from '@gre/api-client';

const fixture: EchoResponse = { message: 'GRE environment fixture', length: 23 };

export default function SetupPage() {
  return <main><h1>{fixture.message}</h1><p>Dependency and production-build verification only.</p></main>;
}

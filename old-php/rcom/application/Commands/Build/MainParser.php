<?php
class Commands_Build_MainParser extends Commands_Lib_Parser{

	/**
	 * Default initial value for the long params accepted by this Command object
	 * params which are not handled by the Parser
	 */
	protected $long_params = array('command:','cleanall::');

	/**
	 * List of parameters this parser can work on/this command can take
	 */
	protected function constructElements(){
		$this->parserElements = self::arrayBuilder(
			new Commands_ParserOption_S($this),
			new Commands_ParserOption_T($this),
			new Commands_ParserOption_F($this),
			new Commands_ParserOption_V($this),
			new Commands_ParserOption_R($this),
			
			new Commands_ParserOption_D($this),
	
			new Commands_ParserOption_All($this)

		);
	}
}//EOF CLASS